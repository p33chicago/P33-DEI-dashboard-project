<script type="ts">
	export let href: string;
</script>

<a
	class="{$$props.class ||
		''} inline-block text-center leading-tight bg-brand-primary-dark-green text-sm sm:text-base text-white border-2 rounded-full font-sans-alternate py-2 sm:py-1 xl:py-2 px-7 sm:px-10 xl:px-12 uppercase w-fit"
	{href}
>
	<slot />
</a>
