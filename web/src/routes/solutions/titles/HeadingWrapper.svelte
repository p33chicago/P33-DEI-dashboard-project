<script type="ts">
	export let always_visible = false;
</script>

<div class="flex text-black font-sans-alternate px-4" class:sm:hidden={!always_visible}>
	<slot />
</div>
