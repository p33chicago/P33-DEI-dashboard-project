<script type="ts">
	export let nohr = false; // <Heading nohr /> to hide the horizontal rule
</script>

<h2
	class="heading {$$restProps.class ||
		''} text-3xl font-sans-alternate capitalize text-brand-primary-dark-green border-light-gray"
	class:border-b-[1px]={!nohr}
	class:mb-2={!nohr}
>
	<slot />
</h2>

<style>
	h2 ~ :global(.heading) {
		margin-top: theme('margin.8');
	}
</style>
