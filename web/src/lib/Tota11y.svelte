<script type="ts">
	import { browser, dev } from '$app/environment';

	if (browser && dev) {
		console.log('Importing tota11y');
		import('@khanacademy/tota11y');
	}
</script>
