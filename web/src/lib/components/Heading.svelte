<script type="ts">
	export let nohr = false; // <Heading nohr /> to hide the horizontal rule
</script>

<h2
	class="heading text-3xl font-sans-alternate capitalize text-brand-primary-dark-green border-light-gray mb-2"
	class:border-b-[1px]={!nohr}
>
	<slot />
</h2>

<style>
	h2 ~ :global(.heading) {
		margin-top: theme('margin.8');
	}
</style>
