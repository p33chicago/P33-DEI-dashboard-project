<script type="ts">
	import { base } from '$app/paths';
	import CTASection from '$lib/components/CTASection.svelte';
	import Takeaway from '$lib/components/Takeaway.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import Scorecard from '$lib/components/scorecard/Scorecard.svelte';
	import type { Scorecard as ScorecardType } from '$lib/domain/Scorecard';
	import Definitions from '$lib/components/scorecard/definitions/Definitions.svelte';
	import TextHighlight from '$lib/components/TextHighlight.svelte';
	import Callout from '$lib/components/Callout.svelte';
	import MapBackground from '$lib/components/MapBackground.svelte';
	import BlockQuote from '$lib/components/BlockQuote.svelte';

	export let data: { scorecard: ScorecardType };
	let { scorecard } = data;
</script>

<svelte:head>
	<title>Tech Equity Index</title>
	<meta
		content="Chicago's collaborative effort to build the most inclusive and equitable tech city in the country."
		name="description"
	/>
</svelte:head>

<!-- HERO -->
<div>
	<div
		class="order-first col-span-1 sm:col-span-4 h-[500px] bg-brand-primary-light-green pt-44 text-center text-2xl"
	>
		<h1>HERO IMAGE WILL GO HERE :)</h1>
	</div>
</div>

<div class="w-full bg-white py-6">
	<BodyContentContainer>
		<!-- top part -->
		<BlockQuote>
			<p class="text-lg lg:text-2xl">
				Skilled tech jobs are fast-growing, companies can’t fill their roles fast enough. Chicago
				can help by addressing lack of equity within their Black and Latin communities. This is our
				effort in how best to support Chicago’s underrepresented communities through different life
				stages. We have gathered data from grade school to college and beyond, as well as offer
				solutions in making Chicago one of the most inclusive cities in the country.
				<TextHighlight>Now, let’s make it happen!</TextHighlight>
			</p>
		</BlockQuote>
	</BodyContentContainer>
</div>
<div class="w-full py-4 bg-white">
	<BodyContentContainer>
		<div>
			<Callout heading="Why Tech Matters">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/why-tech-matters.svg`}
				/>
				We must build an inclusive tech that will bring opportunities and grow Chicago’s economy in the
				next 30 years.
			</Callout>
		</div>
		<div>
			<Callout heading="Why We Built This">
				<img alt="" class="object-scale-down h-8 w-8" slot="image" src={`${base}/why-built.svg`} />
				A shared source of truth for policymakers, businesses, educators and others that provide transparency
				of investments into Chicago’s tech talent.
			</Callout>
		</div>
		<div>
			<Callout heading="What the Data Shows">
				<img alt="" class="object-scale-down h-8 w-8" slot="image" src={`${base}/what-data.svg`} />
				Few black and Latin students lacking math and science in grade school, limited technology access
				in high school and low college enrollment obtain tech career opportunities.
			</Callout>
		</div>
		<div>
			<Callout heading="What is Success">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/what-success.svg`}
				/>
				We believe the process of gathering data is an essential part of working towards greater diversity
				and inclusion in Chicago’s tech economy.
			</Callout>
		</div>
	</BodyContentContainer>
</div>
<MapBackground>
	<BodyContentContainer>
		<div class="col-span-1 sm:col-span-4 text-white pt-4">
			<h1
				class="text-white underline decoration-heads-up-yellow underline-offset-8 text-5xl leading-relaxed"
			>
				Scorecard
			</h1>
			<p class="font-mono">
				The Equity Index score of 0 – 100 measures the gap between how we are serving different
				racial and ethnic populations on tech career pathways. An Equity Index score of 100 would
				indicate that we are providing equal access to all groups and serving them equally well.
				Scores further from 100 indicate our “distance from equity,” with Black and Latino
				populations receiving less access to opportunity and experiencing worse outcomes. Think of
				any score below 90 as a major concern.
			</p>
		</div>
		<Scorecard {scorecard} />
		<div class="text-white sm:col-span-4 bg-black/60 px-8 py-4 bg-blend-multiply my-6 pb-4">
			<Definitions />
		</div>
	</BodyContentContainer>
</MapBackground>
<BodyContentContainer>
	<!-- bottom part -->
	<h3
		class="col-span-1 sm:col-span-4 text-black text-2xl sm:text-4xl leading-relaxed font-sans-alternate sm:mx-8 py-10"
	>
		Black and Latino Chicagoans are dramatically underrepresented in high-paid tech roles after
		receiving fewer quality learning opportunities in school and college
	</h3>

	<!-- Takeaways -->
	<div class="flex col-span-1 sm:col-span-2 py-4">
		<Takeaway heading="47% vs 14%">
			<img height="147" slot="graphic" src={`${base}/diverse-roles.svg`} width="147" />
			<p>
				Nearly half the Cook County population is <TextHighlight left="0.5" top="0.3"
					>Black or Latino</TextHighlight
				>, but those groups get only 14% of the high-skilled tech jobs.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="42% vs 22%">
			<img height="147" slot="graphic" src={`${base}/graduation-hat.svg`} width="147" />
			<p>
				<TextHighlight left="0" top="0.1">Illinois college graduates</TextHighlight> in computing are
				22% Black or Latino despite being 42% of all Illinois high school graduates.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="400% more">
			<img height="147" slot="graphic" src={`${base}/homogenous.svg`} width="147" />
			<p>
				We’re failing kids early. Chicago needs to ensure 9,100 more Black and Latino
				<TextHighlight>8th graders meet math proficiency</TextHighlight> standards to close gaps with
				other groups… And we need to get 5,500 more Black and Latino 8th graders to advanced standards
				to close gaps.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="5,000+">
			<img height="147" slot="graphic" src={`${base}/hands-puzzle.svg`} width="147" />
			<p>
				Access to accelerated opportunities is inequitable: In order to close gaps, Chicago needs to
				get 5,500 more 8th Black and Latino 8th graders to
				<TextHighlight left="0.4" top="0.25">advanced</TextHighlight> standards, and enroll 5,100 more
				Black and Latino students into AP <TextHighlight top="0.1">Computer Science</TextHighlight>.
				Right highlights: "advanced" and "AP Computer Science"
			</p>
		</Takeaway>
	</div>

	<div class="flex col-span-1 sm:col-span-4 rounded-lg bg-brand-primary-light-green/30 my-10">
		<CTASection href="#" link_text="see opportunities" title="What can you do to help?">
			<img class="hidden sm:block w-32 h-48" slot="graphic" src={`${base}/illinois.svg`} />
			<p class="text-mono">
				Every organization can play a role in building a more inclusive TechChicago
			</p>
		</CTASection>
	</div>
</BodyContentContainer>
