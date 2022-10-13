<script type="ts">
	export let always_visible = false;
	$: console.log(always_visible);
</script>

<div class="flex text-black font-sans-alternate px-4" class:sm:hidden={!always_visible}>
	<slot />
</div>
