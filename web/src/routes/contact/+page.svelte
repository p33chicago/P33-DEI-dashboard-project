<script>
	import { browser } from '$app/environment';
	import BannerTitle from '$lib/components/BannerTitle.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
</script>

<svelte:head>
	<script charset="utf-8" src="//js.hsforms.net/forms/embed/v2.js" type="text/javascript"></script>
</svelte:head>

<BannerTitle title="Contact Us" />
<BodyContentContainer>
	<div class="col-span-1 sm:col-span-4 py-8">
		{#if browser}
			<script>
				if (typeof globalThis.hbspt === 'undefined') {
					console.error('Hubspot failed to load');
				}
				globalThis.hbspt.forms.create({
					region: 'na1',
					portalId: '14531327',
					formId: '4f9e2886-8d50-48f9-b770-30624927fb4b'
				});
			</script>
		{/if}
	</div>
</BodyContentContainer>
