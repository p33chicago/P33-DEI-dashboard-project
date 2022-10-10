<script type="ts">
	export let heading: string;
</script>

<div class="flex">
	<slot name="image" />
	<h2 class="font-sans-alternate text-2xl pl-2">{heading}</h2>
</div>
<p class="font-sans text-black pt-4"><slot /></p>
