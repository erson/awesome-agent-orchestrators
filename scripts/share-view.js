// Shared views reference repository names so links survive changes to the catalog order.
const shareControls = ['search', 'category', 'status', 'feature', 'language', 'sort', 'dimension'];
function viewParameters() {
    const params = new URLSearchParams();
    for (const id of shareControls) {
        const value = el(id).value;
        if (value && !(id === 'sort' && value === 'name') && !(id === 'dimension' && value === 'category')) {
            params.set(id, value);
        }
    }
    if (volume) params.set('volume', volume);
    if (page) params.set('page', String(page + 1));
    for (const repo of selected) params.append('compare', repo);
    const mapState = projectMap.exportState();
    if (mapState) params.set('map', mapState);
    return params;
}

function restoreView() {
    const params = new URLSearchParams(location.search);
    for (const id of shareControls) {
        if (!params.has(id)) continue;
        const control = el(id);
        const value = params.get(id);
        if (id === 'search' || [...control.options].some(option => option.value === value)) {
            control.value = value;
        }
    }
    const names = new Set(projects.map(p => p.repo));
    for (const repo of params.getAll('compare')) {
        if (names.has(repo) && selected.size < 4) selected.add(repo);
    }
    volume = ranges.includes(params.get('volume')) ? params.get('volume') : '';
    const requestedPage = Number(params.get('page'));
    page = Number.isSafeInteger(requestedPage) && requestedPage > 0 ? requestedPage - 1 : 0;
    projectMap.restoreState(params.get('map') || '');
}

async function copyView() {
    const url = new URL('https://erson.github.io/orchestration-atlas/');
    url.search = viewParameters().toString();
    url.hash = selected.size ? 'shortlist' : 'directory';
    try {
        await navigator.clipboard.writeText(url.href);
        el('shareStatus').textContent = 'Link copied.';
        el('shareFallback').hidden = true;
    } catch {
        const input = el('shareFallback');
        input.value = url.href;
        input.hidden = false;
        input.focus();
        input.select();
        el('shareStatus').textContent = 'Copy the selected link.';
    }
}
