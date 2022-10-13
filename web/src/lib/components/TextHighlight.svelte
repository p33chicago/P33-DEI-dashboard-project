<script type="ts">
	export let max_offset_x = 0.5;
	export let max_offset_y = 0.5;
	export let left: number = max_offset_x / 5;
	export let top: number = max_offset_y / 3;
	// All dimensions in `rem`
	export let offset_top = Math.min(top, max_offset_y);
	export let offset_bottom = max_offset_y - offset_top;
	export let offset_left = Math.min(left, max_offset_x);
	export let offset_right = max_offset_x - offset_left;
	const rem = (dimension) => `${dimension}rem`;
</script>

<span
	class="{$$props.class || ''} bg-heads-up-yellow border-heads-up-yellow border-opacity-50"
	style:border-bottom-width={rem(offset_bottom)}
	style:border-left-width={rem(offset_left)}
	style:border-right-width={rem(offset_right)}
	style:border-top-width={rem(offset_top)}
	style:margin-bottom={rem(-offset_bottom)}
	style:margin-left={rem(-offset_left)}
	style:margin-right={rem(-offset_right)}
	style:margin-top={rem(-offset_top)}
>
	<slot />
</span>
