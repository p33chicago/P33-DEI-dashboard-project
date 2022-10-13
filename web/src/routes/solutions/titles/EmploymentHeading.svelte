<script>
	import HandshakeIcon from '$lib/components/icons/HandshakeIcon.svelte';
	import HeadingWrapper from './HeadingWrapper.svelte';
</script>

<HeadingWrapper {...$$restProps}>
	<p class="text-xl uppercase">
		<HandshakeIcon class="align-baseline inline mr-2.5" />
		employment
	</p>
</HeadingWrapper>
