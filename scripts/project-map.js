const projectMap = (() => {
  const metrics = {commits_90d: 'Commits (90 days)', contributors: 'Contributors'};
  const special = ['zero-stars', 'missing-stars', 'zero-y', 'missing-y'];
  const boundsNames = ['Minimum stars', 'Maximum stars', 'Minimum activity', 'Maximum activity'];
  let metric = 'commits_90d', selection = '', bounds = [], cohort = [];
  let svg, selector, fields, buckets, notes, pointInfo, resetButton, brush, geometry, plotted;
  let drag = null;

  const number = value => value.toLocaleString('en-US');
  const positive = value => Number.isFinite(value) && value > 0;
  const unknown = value => !Number.isFinite(value) || value < 0;
  function matches(p) {
    const x = p.stars, y = p[metric];
    switch (selection) {
      case 'zero-stars': return x === 0;
      case 'missing-stars': return unknown(x);
      case 'zero-y': return y === 0;
      case 'missing-y': return unknown(y);
      case 'range': return positive(x) && positive(y) &&
        x >= bounds[0] && x <= bounds[1] && y >= bounds[2] && y <= bounds[3];
      default: return true;
    }
  }
  function clear() { metric = 'commits_90d'; selection = ''; bounds = []; }
  function exportState() {
    if (metric === 'commits_90d' && !selection) return '';
    return [metric, selection, ...bounds].join(':');
  }
  function restoreState(value) {
    clear();
    if (typeof value !== 'string' || !value) return;
    const [key, type = '', ...values] = value.split(':');
    if (!Object.hasOwn(metrics, key)) return;
    const nums = values.map(Number);
    if (type === 'range') {
      if (nums.length !== 4 || !nums.every(n => Number.isSafeInteger(n) && n > 0) ||
          nums[1] < nums[0] || nums[3] < nums[2]) return;
    } else if ((type && !special.includes(type)) || nums.length) return;
    metric = key; selection = type; bounds = nums;
  }
  function change(type = '', values = []) {
    selection = type; bounds = values; api.onChange();
  }
  function shape(tag, attributes, content) {
    const n = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [key, val] of Object.entries(attributes)) n.setAttribute(key, val);
    if (content != null) n.textContent = content;
    return n;
  }
  function button(text, fn) {
    const b = node('button', text);
    b.type = 'button'; b.onclick = fn; return b;
  }
  function mount() {
    const root = el('projectMap');
    const header = node('div'), title = node('h3', 'Project map'), axisLabel = node('label', 'Vertical axis');
    header.className = 'chart-head';
    selector = node('select');
    for (const [key, label] of Object.entries(metrics)) selector.add(new Option(label, key));
    selector.onchange = () => { metric = selector.value; change(); };
    axisLabel.append(selector); header.append(title, axisLabel);
    const help = node('p', 'Both axes use a log scale. Drag across points to filter the directory, tap a point, or enter a range.');
    help.className = 'note'; help.id = 'mapHelp';
    svg = shape('svg', {role:'img', 'aria-label':'Project scatter plot', 'aria-describedby':'mapHelp'});
    svg.style.cssText = 'display:block;width:100%;height:290px;touch-action:none;user-select:none;cursor:crosshair';
    svg.onpointerdown = startDrag; svg.onpointermove = move; svg.onpointerup = endDrag;
    svg.onpointercancel = cancelDrag; svg.onlostpointercapture = cancelDrag;
    svg.onpointerleave = () => { if (!drag) pointInfo.textContent = ''; };
    pointInfo = node('p'); pointInfo.className = 'note'; pointInfo.style.minHeight = '1.4em';
    buckets = node('div'); buckets.className = 'toolbar'; buckets.style.justifyContent = 'flex-start';
    for (const key of special) buckets.append(button('', () => change(selection === key ? '' : key)));
    const details = node('details'), form = node('form'), summary = node('summary', 'Enter a range');
    form.className = 'filters';
    fields = boundsNames.map(text => {
      const label = node('label'), caption = node('span', text), input = node('input');
      input.type = 'number'; input.step = '1'; input.min = '1';
      label.append(caption, input); form.append(label); return input;
    });
    const apply = node('button', 'Apply range'); apply.type = 'submit'; form.append(apply);
    form.onsubmit = event => {
      event.preventDefault();
      const defaults = [1, geometry.maxX, 1, geometry.maxY];
      const nums = fields.map((input,i) => input.value === '' ? defaults[i] : input.valueAsNumber);
      for (let i = 0; i < nums.length; i++) {
        if (!Number.isSafeInteger(nums[i]) || nums[i] < 1 || (i % 2 && nums[i] < nums[i-1])) {
          fields[i].setCustomValidity('Enter a positive whole number. Each maximum must be at least its minimum.');
          fields[i].reportValidity(); fields[i].setCustomValidity(''); return;
        }
      }
      change('range', nums);
    };
    details.append(summary, form);
    const footer = node('div'); footer.className = 'toolbar';
    notes = node('p'); notes.className = 'note'; notes.setAttribute('aria-live','polite');
    resetButton = button('Clear map filter', () => change()); footer.append(notes, resetButton);
    root.append(header, help, svg, pointInfo, buckets, details, footer);
    if (typeof ResizeObserver !== 'undefined') {
      new ResizeObserver(() => { if (geometry && geometry.width !== getWidth()) render(cohort); }).observe(svg);
    }
  }
  function getWidth() { return Math.max(240, Math.round(svg.getBoundingClientRect().width) || 640); }
  function position(event) {
    const box = svg.getBoundingClientRect();
    return [Math.max(geometry.left, Math.min(geometry.right, (event.clientX-box.left)*geometry.width/box.width)),
            Math.max(geometry.top, Math.min(geometry.bottom, (event.clientY-box.top)*290/box.height))];
  }
  function nearest(pos) {
    let best, distance = 12;
    for (const dot of plotted) {
      const d = Math.hypot(dot.x-pos[0],dot.y-pos[1]);
      if (d <= distance) { distance = d; best = dot; }
    }
    return best;
  }
  function setBrush(x1,y1,x2,y2) {
    Object.entries({x:Math.min(x1,x2),y:Math.min(y1,y2),width:Math.abs(x1-x2),height:Math.abs(y1-y2)})
      .forEach(([name,value]) => brush.setAttribute(name,value));
    brush.setAttribute('visibility','visible');
  }
  function startDrag(event) {
    if (!event.isPrimary || event.button !== 0) return;
    const box = svg.getBoundingClientRect(), x = (event.clientX-box.left)*geometry.width/box.width;
    const y = (event.clientY-box.top)*290/box.height;
    if (x < geometry.left-4 || x > geometry.right+4 || y < geometry.top-4 || y > geometry.bottom+4) return;
    drag = {start:position(event), id:event.pointerId}; svg.setPointerCapture(event.pointerId);
  }
  function move(event) {
    const pos = position(event);
    if (drag) {
      if (event.pointerId === drag.id) setBrush(...drag.start,...pos);
    } else {
      const dot = nearest(pos);
      pointInfo.textContent = dot ? dot.p.repo+' · '+number(dot.p.stars)+' stars · '+number(dot.p[metric])+' '+metrics[metric].toLowerCase() : '';
    }
  }
  function cancelDrag() {
    if (!drag) return;
    drag = null; render(cohort);
  }
  function endDrag(event) {
    if (!drag || event.pointerId !== drag.id) return;
    const pos = position(event), start = drag.start, g = geometry;
    drag = null;
    if (Math.hypot(pos[0]-start[0],pos[1]-start[1]) < 5) {
      const dot = nearest(pos);
      if (dot) change('range', [dot.p.stars,dot.p.stars,dot.p[metric],dot.p[metric]]);
      else render(cohort);
      return;
    }
    const xAt = x => 10 ** ((x-g.left)/(g.right-g.left)*g.xPower);
    const yAt = y => 10 ** ((g.bottom-y)/(g.bottom-g.top)*g.yPower);
    // Counts are whole numbers. Outward rounding preserves single-pixel and near-axis selections.
    change('range', [Math.max(1,Math.floor(xAt(Math.min(pos[0],start[0])))),
                     Math.ceil(xAt(Math.max(pos[0],start[0]))),
                     Math.max(1,Math.floor(yAt(Math.max(pos[1],start[1])))),
                     Math.ceil(yAt(Math.min(pos[1],start[1])))]);
  }
  function tick(value) {
    if (value >= 1000000) return number(value/1000000)+'m';
    if (value >= 1000) return number(value/1000)+'k';
    return number(value);
  }
  function render(rows) {
    cohort = rows;
    if (!svg) mount();
    selector.value = metric;
    const width = getWidth(), left = 50, right = width-24, top = 18, bottom = 245;
    const extent = key => Math.max(1, Math.ceil(Math.log10(projects.reduce((max,p) =>
      positive(p[key]) ? Math.max(max,p[key]) : max, 1))));
    const xPower = extent('stars'), yPower = extent(metric);
    geometry = {width,left,right,top,bottom,xPower,yPower,maxX:10**xPower,maxY:10**yPower};
    const xPos = val => left+Math.log10(val)/xPower*(right-left);
    const yPos = val => bottom-Math.log10(val)/yPower*(bottom-top);
    svg.setAttribute('viewBox', '0 0 '+width+' 290'); svg.replaceChildren();
    function line(x1,y1,x2,y2) {svg.append(shape('line',{x1,y1,x2,y2,stroke:'#d7ddd6'}));}
    function label(x,y,text,attributes={}) {
      svg.append(shape('text',{x,y,'text-anchor':'middle','font-size':11,fill:'#354740',...attributes},text));
    }
    const xStride = Math.max(1,Math.ceil((xPower+1)*35/(right-left)));
    for (let i=0;i<=xPower;i++) {
      const x=xPos(10**i); line(x,top,x,bottom);
      if (i%xStride===0 || i===xPower) label(x,bottom+17,tick(10**i));
    }
    for (let i=0;i<=yPower;i++) {
      const y=yPos(10**i); line(left,y,right,y); label(left-5,y+4,tick(10**i),{'text-anchor':'end'});
    }
    label((left+right)/2,284,'Stars (log scale)');
    const mid=(top+bottom)/2;
    label(12,mid,metrics[metric]+' (log scale)',{transform:'rotate(-90 12 '+mid+')'});
    plotted = [];
    for (const p of rows) {
      if (!positive(p.stars) || !positive(p[metric])) continue;
      const x=xPos(p.stars), y=yPos(p[metric]);
      plotted.push({p,x,y});
      svg.append(shape('circle',{cx:x,cy:y,r:3.4,fill:matches(p)?'#247657':'#8b9b94',opacity:matches(p)?.69:.27}));
    }
    brush=shape('rect',{fill:'#478565','fill-opacity':.12,stroke:'#294d3b','stroke-width':1.8,visibility:'hidden'});
    svg.append(brush);
    if (selection==='range' && bounds[0]<=geometry.maxX && bounds[2]<=geometry.maxY) {
      setBrush(xPos(bounds[0]),yPos(bounds[2]),xPos(Math.min(bounds[1],geometry.maxX)),yPos(Math.min(bounds[3],geometry.maxY)));
    }
    const labels=['Zero stars','Unknown stars','Zero '+metrics[metric].toLowerCase(),'Unknown '+metrics[metric].toLowerCase()];
    const counts=[rows.filter(p=>p.stars===0).length,rows.filter(p=>unknown(p.stars)).length,
                  rows.filter(p=>p[metric]===0).length,rows.filter(p=>unknown(p[metric])).length];
    [...buckets.children].forEach((b,i)=>{
      b.textContent=labels[i]+' ('+number(counts[i])+')'; b.setAttribute('aria-pressed',String(selection===special[i]));
      b.disabled=!counts[i] && selection!==special[i];
    });
    fields.forEach((input,i)=>{
      input.value=selection==='range'?String(bounds[i]):'';
      input.placeholder=String([1,geometry.maxX,1,geometry.maxY][i]);
      if(i>=2) input.previousElementSibling.textContent=(i===2?'Minimum ':'Maximum ')+metrics[metric].toLowerCase();
    });
    resetButton.disabled=!selection;
    let description=number(plotted.length)+' of '+number(rows.length)+' projects plotted.';
    if(selection==='range') description+=' Selected: '+number(bounds[0])+'–'+number(bounds[1])+' stars, '+
      number(bounds[2])+'–'+number(bounds[3])+' '+metrics[metric].toLowerCase()+'.';
    else if(selection) description+=' Selected: '+labels[special.indexOf(selection)]+'.';
    notes.textContent=description; pointInfo.textContent='';
  }
  const api={render,matches,clear,exportState,restoreState,onChange:()=>{}};
  return api;
})();
