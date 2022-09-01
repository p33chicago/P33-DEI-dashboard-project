<script context="module" lang="ts">
    import { load } from './init.js';
    load();
</script>

<script lang="ts">
	export let id: string;

    let canvas: HTMLElement;

	const render = async () => {
        const Plotly = await load();
        if (!Plotly) {
            return; // server-side
        }
        const { data, layout } = await (await fetch(`/data/${id}.json`)).json();
        await Plotly.newPlot(canvas, data, layout, {responsive: true});
        console.log(Plotly.validate(data, layout));
	};

    console.log('Rendering')
    render();
</script>

<div bind:this={canvas} />
