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
    import Svg from '$lib/figures/k8/noInt.svelte'
    import type {Lifestage} from "$lib/Lifestage.ts";
    import {dev} from '$app/environment';
    import {assets} from "$app/paths";
    import {afterUpdate, onMount} from "svelte";

    export let lifestage: Lifestage['name'];
    export let name: string;

    let container;
    let canvas;

    let data;
    let layout;
    $: loading = true;
    const config = {responsive: true, displayModeBar: false};

    const render = () => {
        if (!Plotly || !data || !layout) {
            // Graph hasn't loaded yet
            return;
        }
        layout.width = canvas.clientWidth
        layout.height = canvas.clientHeight
        Plotly.react(canvas, data, layout, config);
        if (dev) {
            canvas.on('plotly_hover', console.log)
        }
    }

    afterUpdate(() => {
        render();
    })

    onMount(async () => {
        Plotly = await load();
        ({data, layout} = await (await fetch(`${assets}/figures/${lifestage}/${name}.json`)).json());
        loading = false;
    });
</script>

<svelte:window on:resize={render}/>
<div class="flex min-w-[360px] min-h-[200px] h-full w-full overflow-scroll">
    {#if loading }
        <Svg/>
    {:else}
        <div bind:this={canvas}/>
    {/if}
</div>
