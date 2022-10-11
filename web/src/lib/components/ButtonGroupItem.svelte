<!-- Wrap instances of this component in <ButtonGroup /> -->
<script type="ts">
	export let href = '#';
	export let primary = false;
</script>

<a
	class="leading-8 bg-white text-center w-full md:w-auto px-4 uppercase"
	class:bg-brand-primary-dark-green={primary}
	class:text-white={primary}
	{href}
>
	<slot />
</a>
