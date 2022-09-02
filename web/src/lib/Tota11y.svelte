<script type="ts">
import { browser, dev } from '$app/env';

if (browser && dev) {
    console.log('Importing tota11y')
    import('@khanacademy/tota11y');
}
</script>