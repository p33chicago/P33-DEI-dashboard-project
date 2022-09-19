<script>
	import CardPage from "$lib/cards/CardPage.svelte";
</script>

<CardPage>
    <h1>Contact Us</h1>
    <div>
        <p class="px-1 py-6">
            We'd love to chat. 
            Let us know what's on your mind and we'll get back to you asap. 
            Or just provide a way to contact you and we'll keep you in the loop.
        </p>
    </div>
    <div class="w-full">
        <form class="bg-white px-1 pt-6 pb-10 mb-4">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                Name
              </label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Name">
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
              Email
            </label>
            <input class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="email" type="text" placeholder="j.walters@glkh.com">
          </div>
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="message">
              Message
            </label>
            <textarea class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="message" type="text" placeholder="What's on your mind?"/>
          </div>
          <div class="flex items-center justify-between">
            <button class="bg-brand-primary-dark-green text-white py-2 px-4 rounded uppercase" type="button">
              Let us know
            </button>
          </div>
        </form>
      </div>
</CardPage>



