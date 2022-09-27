<script lang="ts">
    import type {Lifestage} from "../domain/Lifestage.ts";
    import {browser} from '$app/environment';
    import ClientSideFigure from "$lib/figure/ClientSideFigure.svelte";
    import ServerSideFigure from "$lib/figure/ServerSideFigure.svelte";

    export let lifestage: Lifestage['name'];
    export let name: string;
</script>

{#if browser}
    <ClientSideFigure {lifestage} {name}/>
{:else}
    <ServerSideFigure {lifestage} {name}/>
{/if}
