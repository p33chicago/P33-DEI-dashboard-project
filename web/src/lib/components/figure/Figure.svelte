<script lang="ts">
	import { browser } from '$app/environment';
	import { assets } from '$app/paths';
	import ClientSideFigure from './ClientSideFigure.svelte';
	import ServerSideFigure from './ServerSideFigure.svelte';

	export let file: string;
	export let svg_only = false;
</script>

{#if browser && svg_only}
	<img alt="" class="w-full" src="{assets}/{file}.svg" />
{:else if browser}
	<ClientSideFigure {file} />
{:else}
	<ServerSideFigure {file} />
{/if}
