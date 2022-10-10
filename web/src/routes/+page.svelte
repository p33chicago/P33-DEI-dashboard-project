<script type="ts">
	import { base } from '$app/paths';
	import CTASection from '$lib/CTASection.svelte';
	import Takeaway from '$lib/Takeaway.svelte';
	import BodyContentContainer from '$lib/BodyContentContainer.svelte';
	import Scorecard from '$lib/scorecard/Scorecard.svelte';
	import type { Scorecard as ScorecardType } from '$lib/domain/Scorecard.ts';
	import Definitions from '$lib/scorecard/definitions/Definitions.svelte';

	export let data: { scorecard: ScorecardType };
	let { scorecard } = data;
</script>

<svelte:head>
	<title>Home</title>
	<meta content="P33" name="description" />
</svelte:head>

<!-- HERO -->
<div>
	<div
		class="order-first col-span-1 sm:col-span-4 h-[500px] bg-brand-primary-light-green pt-44 text-center text-2xl"
	>
		<h1>HERO IMAGE WILL GO HERE :)</h1>
	</div>
</div>

<div class="w-full bg-white">
	<BodyContentContainer>
		<!-- top part -->
		<div class="col-span-1 sm:col-span-4 sans-alternate">
			<p
				class="font-sans-alternate text-black text-lg lg:text-2xl leading-9 px-4 border-l-4 border-heads-up-yellow ml-9 mt-4"
			>
				Skilled tech jobs are fast-growing, companies can’t fill their roles fast enough. Chicago
				can help by addressing lack of equity within their Black and Latin communities. This is our
				effort in how best to support Chicago’s underrepresented communities through different life
				stages. We have gathered data from grade school to college and beyond, as well as offer
				solutions in making Chicago one of the most inclusive cities in the country.
				<span class="bg-heads-up-yellow p-1">Now, let’s make it happen!</span>
			</p>
		</div>
	</BodyContentContainer>
</div>
<div class="w-full py-4 bg-white">
	<BodyContentContainer>
		<div class="ml-12 py-2">
			<div class="flex">
				<img alt="" class="object-scale-down h-8 w-8" src={`${base}/why-tech-matters.svg`} />
				<h2 class="font-sans-alternate text-2xl pl-2">Why Tech Matters</h2>
			</div>
			<p class="font-sans text-black pt-4">
				We must build an inclusive tech that will bring opportunities and grow Chicago’s economy in
				the next 30 years.
			</p>
		</div>
		<div class="ml-12 py-2">
			<div class="flex">
				<img alt="" class="object-scale-down h-8 w-8" src={`${base}/why-built.svg`} />
				<h2 class="font-sans-alternate text-2xl pl-2">Why We Built This</h2>
			</div>
			<p class="font-sans text-black pt-4">
				A shared source of truth for policymakers, businesses, educators and others that provide
				transparency of investments into Chicago’s tech talent.
			</p>
		</div>
		<div class="ml-12 py-2">
			<div class="flex">
				<img alt="" class="object-scale-down h-8 w-8" src={`${base}/what-data.svg`} />
				<h2 class="font-sans-alternate text-2xl pl-2">What the Data Shows</h2>
			</div>
			<p class="font-sans text-black pt-4">
				Few black and Latin students lacking math and science in grade school, limited technology
				access in high school and low college enrollment obtain tech career opportunities.
			</p>
		</div>
		<div class="ml-12 py-2">
			<div class="flex">
				<img alt="" class="object-scale-down h-8 w-8" src={`${base}/what-success.svg`} />
				<h2 class="font-sans-alternate text-2xl pl-2">What is Success</h2>
			</div>
			<p class="font-sans text-black pt-4">
				We believe the process of gathering data is an essential part of working towards greater
				diversity and inclusion in Chicago’s tech economy.
			</p>
		</div>
	</BodyContentContainer>
</div>
<div class="w-full bg-chicago bg-background-map bg-blend-screen bg-repeat text-white py-4">
	<BodyContentContainer>
		<h1
			class="text-white underline decoration-heads-up-yellow underline-offset-8 text-5xl col-span-1 sm:col-span-4"
		>
			Scorecard
		</h1>
		<p class="font-mono col-span-1 sm:col-span-4 pb-6">
			The Equity Index score of 0 – 100 measures the gap between how we are serving different racial
			and ethnic populations on tech career pathways. An Equity Index score of 100 would indicate
			that we are providing equal access to all groups and serving them equally well. Scores further
			from 100 indicate our “distance from equity,” with Black and Latino populations receiving less
			access to opportunity and experiencing worse outcomes. Think of any score below 90 as a major
			concern.
		</p>
		<Scorecard {scorecard} />
		<div class="sm:col-span-4 bg-black/60 px-8 py-4 bg-blend-multiply">
			<Definitions />
		</div>
	</BodyContentContainer>
</div>
<BodyContentContainer>
	<!-- bottom part -->
	<h3
		class="col-span-1 sm:col-span-4 text-black text-4xl leading-relaxed font-sans-alternate mx-8 my-4"
	>
		Black and Latino Chicagoans are dramatically underrepresented in high-paid tech roles after
		receiving fewer quality learning opportunities in school and college
	</h3>

	<!-- Takeaways -->
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="47% vs 14%">
			<img
				class="self-start w-[64px] sm:w-[147px] aspect-square mt-2.5"
				slot="graphic"
				src={`${base}/diverse-roles.svg`}
			/>
			<p>
				Nearly half the Cook County population is Black or Latino, but those groups get only 14% of
				the high-skilled tech jobs.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="42% vs 22%">
			<img
				class="self-start w-[64px] sm:w-[147px] aspect-square"
				slot="graphic"
				src={`${base}/graduation-hat.svg`}
			/>
			<p>
				Illinois college graduates in computing are 22% Black or Latino despite being 42% of all
				Illinois high school graduates.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="400% more">
			<img
				class="self-start w-[64px] sm:w-[147px] aspect-square"
				slot="graphic"
				src={`${base}/homogenous.svg`}
			/>
			<p>
				We’re failing kids early. Chicago needs to ensure 9,100 more Black and Latino 8th graders
				meet math proficiency standards to close gaps with other groups… And we need to get 5,500
				more Black and Latino 8th graders to advanced standards to close gaps.
			</p>
		</Takeaway>
	</div>
	<div class="flex col-span-1 sm:col-span-2">
		<Takeaway heading="5,000+">
			<img
				class="self-start w-[64px] sm:w-[147px] aspect-square"
				slot="graphic"
				src={`${base}/hands-puzzle.svg`}
			/>
			<p>
				Access to accelerated opportunities is inequitable: In order to close gaps, Chicago needs to
				get 5,500 more 8th Black and Latino 8th graders to advanced standards, and enroll 5,100 more
				Black and Latino students into AP Computer Science. Right highlights: "advanced" and "AP
				Computer Science"
			</p>
		</Takeaway>
	</div>

	<div class="flex col-span-1 sm:col-span-4 rounded-lg bg-brand-primary-light-green/30">
		<CTASection href="#" link_text="see opportunities" title="What can you do to help?">
			<img
				class="hidden sm:block w-32 h-48 mix-blend-overlay"
				slot="graphic"
				src={`${base}/chicago.svg`}
			/>
			<p class="text-xl text-mono">
				Every organization can play a role in building a more inclusive TechChicago
			</p>
		</CTASection>
	</div>
</BodyContentContainer>
