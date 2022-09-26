<script context="module" lang="ts">
	import { load } from './init.js';
    import { dev } from '$app/environment';
	load();
</script>

<script lang="ts">
	import type {Lifestage} from "../domain/Lifestage.ts";

    export let lifestage: Lifestage['name'];
    export let name: string;

	let canvas: HTMLElement;
	let config = { responsive: true, displayModeBar: false };

	const render = async () => {
		const Plotly = await load();
		if (!Plotly) {
			return; // server-side
		}
		const { data, layout } = await (await fetch(`/figures/${lifestage}/${name}.json`)).json();
		await Plotly.newPlot(canvas, data, layout, config);
        if (dev) {
            console.log(Plotly.validate(data, layout));
        }
	};
	render();
</script>

<div bind:this={canvas} />
