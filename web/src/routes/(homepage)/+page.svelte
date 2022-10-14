<script type="ts">
	import { assets, base } from '$app/paths';
	import CTASection from '../../lib/components/CTASection.svelte';
	import Takeaway from '../../lib/components/Takeaway.svelte';
	import BodyContentContainer from '../../lib/components/BodyContentContainer.svelte';
	import Scorecard from '../../lib/components/scorecard/Scorecard.svelte';
	import type { Scorecard as ScorecardType } from '../../lib/domain/Scorecard.js';
	import Definitions from '../../lib/components/scorecard/definitions/Definitions.svelte';
	import TextHighlight from '../../lib/components/TextHighlight.svelte';
	import Callout from '../../lib/components/Callout.svelte';
	import MapBackground from '../../lib/components/MapBackground.svelte';
	import BlockQuote from '../../lib/components/BlockQuote.svelte';
	import Hero from './Hero.svelte';

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
<Hero />

<BodyContentContainer>
	<!-- top part -->
	<BlockQuote class="col-span-4 text-lg lg:text-2xl mt-16 sm:-mt-[1.9rem]">
		<p>
			Skilled tech jobs are fast-growing and high-paying. They lift individuals and grow our
			economy. But companies struggle to fill these roles while Black and Latin people have largely
			been kept on the sidelines. Chicago has an opportunity: <TextHighlight>
				Reduce race-based inequality and accelerate economic growth</TextHighlight
			> by diversifying the tech workforce. This is Chicagoland's first effort to understand the full
			picture of what it will take to make Chicago the most inclusive tech city in the country. This
			isn't just a company issue or a pipeline problem: there is critical work to do from grammar school
			to the C-suite.
			<br />
			<TextHighlight>Now, let’s make it happen!</TextHighlight>
		</p>
	</BlockQuote>
</BodyContentContainer>
<div class="py-4">
	<BodyContentContainer>
		<div>
			<Callout heading="Why Tech Matters">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/why-tech-matter-200.svg`}
				/>
				Tech jobs off the best combination of high wages and growing demand. And tech talent is critical
				to Chicago's economic vitality over the next 30 years.
			</Callout>
		</div>
		<div>
			<Callout heading="Why We Built This">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/why-built-200.svg`}
				/>
				We need a shared source of truth about the leakages in the tech talent pipeline and how policymakers,
				businesses and educators can most effectively contribute to improvement.
			</Callout>
		</div>
		<div>
			<Callout heading="What the Data Shows">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/what-data-200.svg`}
				/>
				We fail Black and Latino Chicagoans at every stage from elementary school to career, providing
				weak math and science foundations, few opportunities for enrichment and acceleration, inequitable
				college access, and closed doors at our companies.
			</Callout>
		</div>
		<div>
			<Callout heading="What is Success">
				<img
					alt=""
					class="object-scale-down h-8 w-8"
					slot="image"
					src={`${base}/what-sucess-200.svg`}
				/>
				The ultimate goal is for Chicagoland's tech workforce to reflect the racial, ethnic and gender
				demographics of the region. For now, we celebrate the collective effort to confront the inequities
				the data reveals.
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
		<div
			class="text-white col-span-1 sm:col-span-4 bg-black/60 px-8 py-4 bg-blend-multiply lg:mt-6 mb-6 pb-4"
		>
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
		<Takeaway heading="9,000+">
			<img height="147" slot="graphic" src={`${base}/falling.svg`} width="147" />
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
				<TextHighlight left="0.4" top="0.25">advanced</TextHighlight> math standards, and enroll 5,100
				more Black and Latino students into AP <TextHighlight top="0.1"
					>Computer Science</TextHighlight
				>.
			</p>
		</Takeaway>
	</div>

	<div class="flex col-span-1 sm:col-span-4 rounded-lg bg-brand-primary-light-green/30 my-10">
		<CTASection href="{base}/contact" link_text="Contact Us" title="What can you do to help?">
			<img class="hidden sm:block w-32 h-48" slot="graphic" src={`${base}/illinois.svg`} />
			<p class="text-mono">
				Every organization can play a role in building a more inclusive TechChicago
			</p>
		</CTASection>
	</div>
</BodyContentContainer>

<div class="bg-light-gray/20 py-6 text-center space-y-2 border border-dark-gray/20">
	<p class="font-sans-alternate text-2xl">Our Contributing Partner</p>
	<img
		alt="Thoughtworks"
		class="inline-block"
		height="48"
		src="{assets}/thoughtworks.svg"
		width="302"
	/>
</div>
