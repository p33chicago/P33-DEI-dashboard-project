<script type="ts">
	import { browser } from '$app/environment';
	import BannerTitle from '$lib/components/BannerTitle.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';

	const load_hubspot = () => {
		const script = document.createElement('script');
		script.type = 'text/javascript';
		script.addEventListener('load', load_form);
		script.src = 'https://js.hsforms.net/forms/embed/v2.js';
		document.head.appendChild(script);
	};
	const load_form = () => {
		window.hbspt.forms.create({
			target: '.contact-form',
			region: 'na1',
			portalId: '14531327',
			formId: '4f9e2886-8d50-48f9-b770-30624927fb4b'
		});
	};

	if (browser) {
		load_hubspot();
	}
</script>

<svelte:head>
	<title>Contact Us</title>
	<meta
		content="How to get involved or learn more about building an inclusive and equitable tech economy in Chicago."
		name="description"
	/>
	<link href="https://js.hsforms.net" rel="preconnect" />
	<link href="https://js.hsforms.net/forms/embed/v2.js" rel="prefetch" />
</svelte:head>

<BannerTitle title="Contact Us" />
<BodyContentContainer>
	<div class="contact-form text-black col-span-1 sm:col-span-4 py-8">
		<div class="bg-really-light-gray h-[600px] w-full max-w-[calc(42rem-8px)]" id="skeleton">
			<!-- loading placeholder -->
		</div>
	</div>
</BodyContentContainer>

<style>
	#skeleton {
		animation: skeleton-loading 1s linear infinite alternate;
	}

	@keyframes skeleton-loading {
		0% {
			background-color: theme('colors.white');
		}
		100% {
			background-color: theme('colors.light-gray');
		}
	}

	.contact-form :global(fieldset) {
		max-width: theme('maxWidth.2xl');
	}
	.contact-form :global(fieldset):not([hidden]) + :global(fieldset):not([hidden]),
	.contact-form :global(fieldset):not([hidden]) + :global(.hs-submit):not([hidden]) {
		margin-top: theme('margin.8');
	}

	:global(.hs-form-required) {
		color: theme('colors.fail-red');
		padding-left: theme('padding.1');
	}

	:global(.hs-error-msgs) {
		color: theme('colors.fail-red');
	}

	.contact-form :global(input):not([type='button'], [type='submit']),
	.contact-form :global(select),
	.contact-form :global(textarea) {
		background-color: theme('backgroundColor.really-light-gray');
		border-radius: 0;
		border-bottom: 2px solid theme('colors.brand-primary-dark-green');
		line-height: theme('lineHeight.loose');
		padding-left: theme('padding.4');
		padding-right: theme('padding.4');
	}
	.contact-form
		:global(input):not([type='button'], [type='submit'], [type='radio'], [type='checkbox']),
	.contact-form :global(select),
	.contact-form :global(textarea) {
		width: 100% !important;
	}

	.contact-form :global(select) {
		height: 2rem;
	}
	.contact-form :global(textarea) {
		resize: vertical;
	}
	.contact-form :global(input[type='button']),
	.contact-form :global(input[type='submit']) {
		/* inline-block leading-10 bg-brand-primary-dark-green text-white border-2 rounded-full font-sans-alternate mt-3.5 px-8 sm:px-11 uppercase */
		line-height: theme('lineHeight.relaxed');
		background-color: theme('backgroundColor.brand-primary-dark-green');
		color: theme('textColor.white');
		border-width: theme('borderWidth.2');
		border-radius: theme('borderRadius.full');
		font-family: theme('fontFamily.sans-alternate'), serif;
		padding-left: theme('padding.11');
		padding-right: theme('padding.11');
		text-transform: uppercase;
	}

	.contact-form :global(input[type='radio']),
	.contact-form :global(input[type='checkbox']) {
		margin-right: theme('margin.2');
	}
</style>
