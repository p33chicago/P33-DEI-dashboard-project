<input class="side-menu" type="checkbox" id="side-menu" />
<label class="hamb" for="side-menu"><span class="hamb-line" /></label>
<nav>
	<!-- <svg viewBox="0 0 2 3" aria-hidden="true">
        <path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
    </svg>
    <ul>
        <li class:active={$page.url.pathname === '/'}><a sveltekit:prefetch href="/">Home</a></li>
    </ul>
    <svg viewBox="0 0 2 3" aria-hidden="true">
        <path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
    </svg> -->

	<ul>
		<li><a href="/">The Data</a></li>
		<li><a href="/methodology">Methodology</a></li>
		<li><a href="/resources">Resources</a></li>
		<li><a href="/about">About Us</a></li>
		<li><a href="/partners">Our Partners</a></li>
		<li><a href="/contact">Contact Us</a></li>
	</ul>
</nav>

<style>
	nav {
		display: flex;
		justify-content: center;
		/* --background: rgba(255, 255, 255, 0.7); */
	}

	/* svg {
		width: 2em;
		height: 3em;
		display: block;
	} */

	/* path {
		fill: var(--background);
	} */

	ul {
    width: 100%;
    height: 100%;
    position: fixed;
    background-color: var(--background);
    overflow: hidden;
    max-height: 0;
    transition: max-height .5s ease-out;
		/* position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain; */
	}

	li {
    display: block;
    padding: 30px;
    /* color: var(--white); */
		/* position: relative;
		height: 100%; */
	}
	/* 
	li.active::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--accent-color);
	} */

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 1em;
		/* color: var(--heading-color); */
		color: #0db196;
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: capitalize;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--accent-color);
	}

	.hamb {
		cursor: pointer;
		float: right;
		padding: 40px 20px;
	} /* Style label tag */

	.hamb-line {
		background: var(--text-color);
		display: block;
		height: 2px;
		position: relative;
		width: 24px;
	} /* Style span tag */

	.hamb-line::before,
	.hamb-line::after {
		background: var(--text-color);
		content: '';
		display: block;
		height: 100%;
		position: absolute;
		transition: all 0.2s ease-out;
		width: 100%;
	}
	.hamb-line::before {
		top: 5px;
	}
	.hamb-line::after {
		top: -5px;
	}

	.side-menu {
		display: none;
	}
	.side-menu:checked ~ nav {
		max-height: 100%;
	}
	.side-menu:checked ~ .hamb .hamb-line {
		background: transparent;
	}
	.side-menu:checked ~ .hamb .hamb-line::before {
		transform: rotate(-45deg);
		top: 0;
	}
	.side-menu:checked ~ .hamb .hamb-line::after {
		transform: rotate(45deg);
		top: 0;
	}
	@media (min-width: 768px) {
		nav {
			max-height: none;
			top: 0;
			position: relative;
			float: right;
			width: fit-content;
		}
		ul li {
			float: left;
		}
		ul a:hover {
			background-color: transparent;
			color: var(--gray);
		}

		.hamb {
			display: none;
		}
	}
</style>
