<script>
	import MortarboardCapIcon from '$lib/components/icons/MortarboardCapIcon.svelte';
	import HeadingWrapper from './HeadingWrapper.svelte';
</script>

<HeadingWrapper {...$$restProps}>
	<p class="text-xl uppercase">
		<MortarboardCapIcon class="align-baseline inline mr-2.5" />
		college
	</p>
</HeadingWrapper>
