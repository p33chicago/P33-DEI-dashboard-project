<script context="module" lang="ts">
    import {load} from './init.js';

    load();
</script>

<script lang="ts">
    import type {Lifestage} from "../domain/Lifestage.ts";
    import {browser} from '$app/environment';
    import {assets} from '$app/paths';
    import fs from 'fs';

    export let lifestage: Lifestage['name'];
    export let name: string;

    let canvas;
    let config = {responsive: true, displayModeBar: false};
    let svg;
    const render = async () => {
        if (browser) {
            const Plotly = await load();
            const {data, layout} = await (await fetch(`${assets}/figures/${lifestage}/${name}.json`)).json();
            await Plotly.newPlot(canvas, data, layout, config);
        } else {
            svg = fs.readFileSync(`static/figures/${lifestage}/${name}.svg`, 'utf-8');
            console.log(svg)
        }
        // console.log(htmlContent)
    };
    render();
</script>

{#if browser}
    <div bind:this={canvas}></div>
{:else}
    <svg>{@html svg}</svg>
{/if}

<style>
    div, svg {
        width: 100%;
        /*height: 100%;*/
        aspect-ratio: 1/1;
    }
</style>