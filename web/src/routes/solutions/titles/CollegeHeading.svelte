<script>
	import MortarboardCapIcon from '$lib/components/icons/MortarboardCapIcon.svelte';
	import HeadingWrapper from './HeadingWrapper.svelte';
</script>

<HeadingWrapper {...$$restProps}>
	<h3 class="text-black text-xl uppercase">
		<MortarboardCapIcon class="align-baseline inline mr-2.5" />
		college
	</h3>
</HeadingWrapper>
