<script>
	import BannerTitle from '$lib/components/BannerTitle.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import Heading from '$lib/components/Heading.svelte';
	import BlockQuote from '$lib/components/BlockQuote.svelte';
	import P33Logo from '$lib/components/P33Logo.svelte';
	import { assets } from '$app/paths';
	import PartnerLogo from '$lib/components/PartnerLogo.svelte';
</script>

<svelte:head>
	<title>About</title>
	<meta
		content="A dozen Chicago organizations are collaborating to build a more equitable Chicago technology economy."
		name="description"
	/>
</svelte:head>

<BannerTitle title="About" />
<BodyContentContainer>
	<div class="sm:col-span-4 py-8">
		<Heading>Our Vision</Heading>
		<div class="my-6">
			<BlockQuote>
				<p class="text-2xl lg:text-5xl">
					Chicago will be the country’s most inclusive tech city, with a tech workforce that
					reflects the racial, ethnic and gender makeup of the Chicagoland region.
				</p>
			</BlockQuote>
		</div>

		<Heading nohr>Our Mission</Heading>
		<ol class="list-decimal list-inside">
			<li>
				To present an honest diagnosis of system-level performance in helping all students succeed
				on a learning-to-career journey into the digital economy;
			</li>
			<li>To identify the most important problems to address;</li>
			<li>To offer ambitious but practicable solutions to these problems; and</li>
			<li>Mobilize all stakeholders in the region to pursue those solutions.</li>
		</ol>
		<p>
			This effort is not intended to tell positive stories about Chicago; we anticipate sharing
			uncomfortable data and stories through this effort. However, we believe the process of
			gathering and acting upon such sobering data is part of the positive story of Chicago working
			towards greater diversity and inclusion in its tech economy.
		</p>

		<Heading nohr>Who We Are</Heading>
		<p>
			This is a partnership of several organizations collaborating on a common goal of building a
			tech workforce that reflects the region, and creating inclusive learning and working
			environments where all Chicagolanders can thrive. All of our organizations share some
			combination of interest in Chicago, the technology economy, and diversity, equity and
			inclusion. And we believe that we’re more likely to reach our destination by being honest
			about the challenges that lie ahead and working together to solve them.
		</p>
		<div class="my-6">
			<P33Logo class="float-none sm:float-left mt-2" />
			<p class="sm:ml-[120px]">
				<a href="https://p33chicago.com" target="_blank">P33</a> leads and coordinates this effort
				on behalf of the partnership and the region. P33 is a business-led nonprofit founded in 2019
				to make Chicago a tier-one tech city and foster inclusive economic growth. The organization
				focuses on growing a diverse tech workforce in collaboration with its Tech Talent Alliance
				of 50 companies; and supporting start-up founders with funding, support and connections to
				founders through initiatives such as
				<a href="https://techrise.co/" target="_blank">TechRise</a>, a weekly pitch competition that
				distributes non-dilutive capital to Black and Latino founders and women.
			</p>
		</div>
		<div
			class="my-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-y-16 sm:gap-y-12 justify-items-center "
		>
			<PartnerLogo
				alt="GET Cities"
				height="78"
				src="{assets}/partner_logos/GETlogo_Cities_vertical@1000px (6).png"
				width="120"
			/>
			<PartnerLogo
				alt="Chicago United"
				height="85"
				src="{assets}/partner_logos/CU Logo +Tagline - Copy.jpg"
				width="215"
			/>
			<PartnerLogo
				alt="Partnership for College Completion"
				height="77"
				src="{assets}/partner_logos/2022 PCC Logo-transparent.png"
				width="289"
			/>
			<PartnerLogo
				alt="Education Systems Center"
				height="78"
				src="{assets}/partner_logos/EdSystems 10 Year - Horizontal.svg"
				width="248"
			/>
			<PartnerLogo
				alt="Illinois Science & Technology Coalition"
				height="114"
				src="{assets}/partner_logos/ISTCLogo-H1.png"
				width="226"
			/>
			<PartnerLogo
				alt="Latinas in Tech"
				height="125"
				src="{assets}/partner_logos/LatinasInTech_Logo_500 1.png"
				width="125"
			/>
			<PartnerLogo
				alt="Digital Youth Network"
				height="110"
				src="{assets}/partner_logos/DYN_Logo.png"
				width="205"
			/>
			<PartnerLogo
				alt="Illinois Workforce and Education Research Collaborative"
				height="105"
				src="{assets}/partner_logos/IWERC - white background.png"
				width="156"
			/>
			<PartnerLogo
				alt="UChicago Consortium on School Research"
				height="36"
				src="{assets}/partner_logos/UCSR_PrimaryLogo_FullColor_RGB.png"
				width="309"
			/>
		</div>
	</div>
</BodyContentContainer>
