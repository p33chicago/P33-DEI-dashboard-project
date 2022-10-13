<script>
	import CertificateIcon from '$lib/components/icons/CertificateIcon.svelte';
	import HeadingWrapper from './HeadingWrapper.svelte';
</script>

<HeadingWrapper {...$$restProps}>
	<p class="text-xl uppercase">
		<CertificateIcon class="align-baseline inline mr-2.5" />
		high school
	</p>
</HeadingWrapper>
