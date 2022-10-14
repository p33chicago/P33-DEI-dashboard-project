<script>
	import SpaceshipIcon from '$lib/components/icons/SpaceshipIcon.svelte';
	import HeadingWrapper from './HeadingWrapper.svelte';
</script>

<HeadingWrapper {...$$restProps}>
	<h3 class="text-black text-xl uppercase">
		<SpaceshipIcon class="align-baseline inline mr-2.5" />
		k-8
	</h3>
</HeadingWrapper>
