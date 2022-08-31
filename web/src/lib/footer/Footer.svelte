<footer>
	<p>Footer stuff goes here</p>
</footer>

<style>
    footer {
        display: flex;
        flex-direction: column;
		justify-content: center;
        align-items: center;
        /* border-top: 2px solid #b1b3b4; */
        padding: 30px;
        background: theme('colors.brand-primary-green');
    }

    footer p {
        color: theme('colors.white');
    }

    @media (min-width: 480px) {
		footer {
			padding: 40px 0;
		}
	}
</style>