<script>
	import BannerTitle from '$lib/components/BannerTitle.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import SpaceshipIcon from '$lib/components/icons/SpaceshipIcon.svelte';
	import CertificateIcon from '$lib/components/icons/CertificateIcon.svelte';
	import MortarboardCapIcon from '$lib/components/icons/MortarboardCapIcon.svelte';
	import HandshakeIcon from '$lib/components/icons/HandshakeIcon.svelte';
</script>

<svelte:head>
	<title>Solutions</title>
	<meta content="Recommendations for how to improve diversity, equity and inclusion in Chicago's tech economy." name="description" />
</svelte:head>

<BannerTitle subtitle="" title="Solutions" />
<div class="bg-white">
	<BodyContentContainer>
		<div class="col-span-4">
			<p>
				SOLUTIONS! Pariatur tacos messenger bag squid post-ironic ut quis you probably haven't heard
				of them. Vinyl laboris umami plaid vaporware elit 90's gatekeep yes plz hoodie letterpress
				trust fund proident. Enim cillum migas brunch. Schlitz ramps ethical neutra.
			</p>
		</div>
		<hr class="col-span-4 border-1 border-light-gray py-4" />
		<!-- first row -->
		<div class="col-span-4 grid grid-cols-5 gap-2">
			<div
				class="bg-brand-primary-really-light-green bg-topography border-b-4 border-brand-primary-green drop-shadow-md uppercase text-center text-black font-sans-alternate"
			>
				<p class="underline decoration-heads-up-yellow decoration-4 underline-offset-8">strategy</p>
			</div>
			<!--K8 -->
			<div class="k8 border-b-2 border-light-gray">
				<div class="flex text-black font-sans-alternate p-4">
					<p class="text-xl uppercase">
						<SpaceshipIcon class="align-baseline inline mr-2.5" />
						k-8
					</p>
				</div>
				<p class="px-4">
					<span class="text-brand-primary-green">Start early.</span> Quality math instruction and out-of-school
					enrichment opportunities will build the foundation for later success.
				</p>
			</div>
			<!--Highschool -->
			<div class="highschool border-b-2 border-light-gray">
				<div class="flex text-black font-sans-alternate p-4">
					<p class="text-xl uppercase">
						<CertificateIcon class="align-baseline inline mr-2.5" />
						high school
					</p>
				</div>
				<p class="px-4">
					<span class="text-brand-primary-green">Aim high.</span> Expand access to advanced STEM programs
					in high school, and complement with out-of-school enrichment opportunities.
				</p>
			</div>
			<!--College -->
			<div class="college border-b-2 border-light-gray">
				<div class="flex text-black font-sans-alternate p-4">
					<p class="text-xl uppercase">
						<MortarboardCapIcon class="align-baseline inline mr-2.5" />
						college
					</p>
				</div>
				<p class="px-4">
					<span class="text-brand-primary-green">Focus on education and employment.</span> Target support
					for underrepresented students to complete STEM degrees, and partner with companies for work-based
					learning experiences starting freshman year.
				</p>
			</div>
			<!--Employment -->
			<div class="employment border-b-2 border-light-gray border-t-2">
				<div class="flex text-black font-sans-alternate p-4">
					<p class="text-xl uppercase">
						<HandshakeIcon class="align-baseline inline mr-2.5" />
						employment
					</p>
				</div>
				<p class="px-4">
					<span class="text-brand-primary-green">Open the aperture.</span> Hire tech talent from a wider
					group of colleges and training providers—and increase the number of hires from those places.
				</p>
			</div>
		</div>
		<!-- second row -->
		<div class="col-span-4 grid grid-cols-5 gap-2">
			<div
				class="bg-brand-primary-really-light-green bg-topography border-b-4 border-brand-primary-green drop-shadow-md uppercase text-center text-black font-sans-alternate"
			>
				<p class="underline decoration-heads-up-yellow decoration-4 underline-offset-8">
					recommendations
				</p>
			</div>
			<!--K8 -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li class="pb-4">
						1. Improve school access to quality math and science through funding and policy reform.
					</li>
					<li class="pb-4">
						2. Expand student access to after school and summer opportunities in STEM through
						funding and partnerships.
					</li>
					<li class="pb-4">3. Offer exploring computer science (ECS) in junior high.</li>
				</ul>
			</div>
			<!--Highschool -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li class="pb-4">1. Improve Algebra and Calculus education across the district.</li>
					<li class="pb-4">
						2. Enroll more Black and Latin students in AP computer science and other advanced
						programs by investing in teacher PD and certification.
					</li>
					<li class="pb-4">
						3. Fund and partner with nonprofits and companies to bring enrichment opportunities to
						high school students.
					</li>
				</ul>
			</div>
			<!--College -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li class="pb-4">
						1. Implement student success programs and cash support to ensure low-income students
						complete STEM degrees.
					</li>
					<li class="pb-4">
						2. Start work-based learning and mentorship freshman year in partnership with companies.
					</li>
				</ul>
			</div>
			<!--Employment -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li class="pb-4">1. Improve algebra and calculus education across the district.</li>
					<li class="pb-4">
						2. Enroll more Black and Latin students in AP Computer Science and other advanced
						programs by investing in teacher PD and certification.
					</li>
					<li class="pb-4">
						3. Fund and partner with nonprofits and companies to bring enrichment opportunities to
						high school students.
					</li>
				</ul>
			</div>
		</div>
		<!-- third row -->
		<div class="col-span-4 grid grid-cols-5 gap-2">
			<div
				class="bg-brand-primary-really-light-green bg-topography border-b-4 border-brand-primary-green drop-shadow-md uppercase text-center text-black font-sans-alternate"
			>
				<p class="underline decoration-heads-up-yellow decoration-4 underline-offset-8">
					organization
				</p>
			</div>
			<!--K8 -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li>- PLACEHOLDER</li>
					<li>- PLACEHOLDER</li>
					<li>- PLACEHOLDER</li>
				</ul>
			</div>
			<!--Highschool -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li>- Project Exploration</li>
					<li>- ISTC</li>
					<li>- CodeNation</li>
					<li>- Microsoft TEALS</li>
					<li>- Project Syncere</li>
					<li>- CLX</li>
				</ul>
			</div>
			<!--College -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li>Programs:</li>
					<li>- Parker-Dewey</li>
					<li>- P33 Strong Start</li>
					<li>- Braven</li>
					<li>- Breakthrough Tech</li>
					<li>- Advocacy:</li>
					<li>- Young Invincibles</li>
					<li>- AnitaB</li>
					<li>- Advance Illinois</li>
					<li>- Women Employed</li>
					<li>- PCC</li>
				</ul>
			</div>
			<!--Employment -->
			<div class="border-b-2 border-light-gray">
				<ul class="p-4">
					<li>To hire non-grad talent:</li>
					<li>- Nonprofits: I.C.Stars, Per Scholas, National Able</li>
					<li>- Bootcamps/Etc: Bitwise, General Assembly, Tech Elevator</li>
					<li>- DPI</li>
					<li>
						To build more inclusive tech cultures: Latinas in Tech, HACE, AnitaB, BWISE, Chicago
						United, GET Cities
					</li>
				</ul>
			</div>
		</div>
	</BodyContentContainer>
</div>

<style>
	.k8 {
		border-top: 10px solid theme('colors.warn-orange');
	}
	.highschool {
		border-top: 10px solid theme('colors.blue');
	}
	.college {
		border-top: 10px solid theme('colors.fail-red');
	}
	.employment {
		border-top: 10px solid theme('colors.green');
	}
</style>
