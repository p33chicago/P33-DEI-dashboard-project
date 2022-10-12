<script type="ts">
	import { base } from '$app/paths';
</script>

<ul class="flex justify-center xl:justify-start divide-x divide-light-gray">
	<li><a class="px-1 sm:px-2 whitespace-nowrap" href={base}>Home</a></li>
	<li><a class="px-1 sm:px-2 whitespace-nowrap" href="{base}/scorecard">Scorecard</a></li>
	<li><a class="px-1 sm:px-2 whitespace-nowrap" href="{base}/solutions">Solutions</a></li>
	<li><a class="px-1 sm:px-2 whitespace-nowrap" href="{base}/about">About Us</a></li>
	<li><a class="px-1 sm:px-2 whitespace-nowrap" href="{base}/contact">Contact Us</a></li>
</ul>

<style>
	a {
		color: theme('colors.white');
	}
</style>
