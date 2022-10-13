<script type="ts">
	import Button from '$lib/components/Button.svelte';

	export let title: string;
	export let href: string;
	export let link_text: string;
</script>

<slot name="graphic" />
<div class="px-9 py-7">
	<h2 class="text-3xl font-sans-alternate text-black">{title}</h2>
	<slot />
	<Button class="min-w-full sm:min-w-fit mt-3.5" {href}>{link_text}</Button>
</div>
