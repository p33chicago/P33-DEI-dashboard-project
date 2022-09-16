<script context="module" lang="ts">
	import { load } from './init.js';
    import { dev } from '$app/environment';
	load();
</script>

<script lang="ts">
	export let id: string;

	let canvas: HTMLElement;
	let config = { responsive: true, displayModeBar: false };

	const render = async () => {
		const Plotly = await load();
		if (!Plotly) {
			return; // server-side
		}
		const { data, layout } = await (await fetch(`/data/${id}.json`)).json();
		await Plotly.newPlot(canvas, data, layout, config);
        if (dev) {
            console.log(Plotly.validate(data, layout));
        }
	};
	render();
</script>

<div bind:this={canvas} />
