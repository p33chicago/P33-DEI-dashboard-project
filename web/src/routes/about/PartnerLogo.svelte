<script type="ts">
	export let src: string;
	export let alt: string | undefined = '';
	export let href: string | undefined;
</script>

{#if href}
	<a {href} target="_blank" class="ml-auto mr-auto sm:ml-0 sm:mr-0">
		<img {alt} {src} {...$$restProps} />
	</a>
{:else}
	<img {alt} {src} {...$$restProps} class="ml-auto mr-auto sm:ml-0 sm:mr-0" />
{/if}
