<script type="ts">
	export let href: string;
</script>

<a
	class="{$$props.class ||
		''} inline-block leading-10 bg-brand-primary-dark-green text-white border-2 rounded-full font-sans-alternate px-8 sm:px-11 uppercase"
	{href}
>
	<slot />
</a>
