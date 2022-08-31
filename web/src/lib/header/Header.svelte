<script lang="ts">
	import { page } from '$app/stores';
	// import Nav from './Nav.svelte'
</script>

<header>
	<div class="corner">
		<a href="/">P33</a>
	</div>

	<!-- <Nav /> -->
	<nav>
		<ul>
			<li><a href="/">The Data</a></li>
			<li><a href="/methodology">Methodology</a></li>
			<li><a href="/resources">Resources</a></li>
			<li><a href="/about">About Us</a></li>
			<li><a href="/partners">Our Partners</a></li>
			<li><a href="/contact">Contact Us</a></li>
		</ul>
	</nav>

	<div class="corner">
		<!-- TODO put something else here? github link? -->
	</div>
</header>

<style>
	header {
		display: flex;
		background: theme('colors.brand-primary-light-green');	
	}

	.corner {
		width: 3em;
		height: 3em;
	}

	.corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
		color: theme('colors.white');
		text-decoration: none;
	}

	.corner a:hover {
		border: none;
	}

	/* .corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	} */

	nav {
		display: flex;
		justify-content: center;
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 1em;
		color: theme('colors.white');
		font-weight: theme('fontWeight.default-regular');
		font-size: 0.8rem;
		text-transform: capitalize;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		font-weight: theme('fontWeight.default-bold');
		border-bottom: 1px solid theme('colors.white');
	}
</style>
