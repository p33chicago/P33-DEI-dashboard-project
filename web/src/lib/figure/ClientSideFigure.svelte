<script context="module" lang="ts">
    let Plotly: typeof import('plotly.js');

    const load = async (): Promise<typeof Plotly> => {
        if (!Plotly) {
            Plotly = await import('plotly.js/dist/plotly-basic.min.js');
        }
        if (!Plotly) {
            throw Error('Could not load Plotly');
        }
        return Plotly;
    };
</script>

<script lang="ts">
    import type {Lifestage} from "../domain/Lifestage.ts";
    import {assets} from '$app/paths';

    export let lifestage: Lifestage['name'];
    export let name: string;

    let canvas;
    let data;
    let layout;
    const config = {responsive: true, displayModeBar: false};

    const render = () => {
        if (!Plotly || !data || !layout) {
            // Graph hasn't loaded yet
            return;
        }
        layout.width = canvas.clientWidth
        layout.height = canvas.clientHeight
        console.log(layout)
        Plotly.react(canvas, data, layout, config);
    }

    const init = async () => {
        Plotly = await load();
        ({data, layout} = await (await fetch(`${assets}/figures/${lifestage}/${name}.json`)).json());
        render();
    };
    init();
</script>

<svelte:window on:resize={render}/>
<div bind:this={canvas} class="w-full h-full"></div>

<style>
    div {
        width: 100%;
        aspect-ratio: 1/1;
        overflow: auto;
    }
</style>