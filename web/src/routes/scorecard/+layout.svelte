<script type="ts">
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import BannerTitle from '$lib/components/BannerTitle.svelte';
</script>

<svelte:head>
	<title>Scorecard</title>
</svelte:head>

<BannerTitle
	subtitle="Equity index scorecard"
	title="Kindergarten-8th, High School, College, Career"
/>

<div class="pt-8 bg-background-map">
	<BodyContentContainer>
		<slot />
	</BodyContentContainer>
</div>
