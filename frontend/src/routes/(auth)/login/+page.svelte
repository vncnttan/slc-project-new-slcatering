<script lang="ts">
    import Particle from "../../../components/Particle.svelte";
    import slcatering_logo from "$lib/assets/slcatering_logo.png";
    import {toast} from "@zerodevx/svelte-toast";
    import {Builder} from "xml2js";
    import axios from "axios";

    let usernameIcon: HTMLElement | null = null;
    let passwordIcon: HTMLElement | null = null;
    let usernameInput = "";
    let passwordInput = "";

    const usernameFocus = () => {
        usernameIcon?.classList.remove("text-gray-500")
        usernameIcon?.classList.add("text-red-sig")
    }
    const usernameBlur = () => {
        usernameIcon?.classList.remove("text-red-sig")
        usernameIcon?.classList.add("text-gray-500")
    }

    const passwordFocus = () => {
        passwordIcon?.classList.remove("text-gray-500")
        passwordIcon?.classList.add("text-red-sig")
    }

    const passwordBlur = () => {
        passwordIcon?.classList.remove("text-red-sig")
        passwordIcon?.classList.add("text-gray-500")
    }


    const builder = new Builder();
    // const xmls = builder.buildObject({
    //     'soap:Envelope': {
    //         $: {
    //             'xmlns:soap': 'http://www.w3.org/2003/05/soap-envelope',
    //             'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    //             'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
    //         },
    //         'soap:Body': {
    //             'LogOn': {
    //                 $: {
    //                     xmlns: 'http://bluejack.binus.ac.id/lapi/api/Account'
    //                 },
    //                 'username': usernameInput,
    //                 'password': passwordInput
    //             }
    //         }
    //     }
    // });
    let xmls='<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\
                            xmlns:web="http://www.webserviceX.NET/">\
            <soapenv:Header/>\
            <soapenv:Body>\
              <web:ConversionRate>\
                <web:FromCurrency>INR</web:FromCurrency>\
                <web:ToCurrency>USD</web:ToCurrency>\
              </web:ConversionRate>\
            </soapenv:Body>\
          </soapenv:Envelope>';

    async function onSubmit(e: SubmitEvent) {
        e.preventDefault();

        if (usernameInput.length < 1 || passwordInput.length < 1) {
            toast.push("All fields must be filled", {
                theme: {
                    "--toastBackground": "#B02000",
                    "--toastColor": "#fff",
                    "--toastProgressBackground": "#fff",
                    "--toastProgressColor": "#B02000"
                }
            })
        }

        try {
            // const res = await axios.post("https://bluejack.binus.ac.id/lapi/api/Account/LogOn", {
            //     username: usernameInput,
            //     password: passwordInput
            // }, {
            //     withCredentials: true
            // });
            // const response = await axios.post('https://bluejack.binus.ac.id/lapi/api/Account/LogOn', xmls, {
            //     headers: { 'Content-Type': 'text/xml' },
            //     withCredentials: true
            // });
            // const data = response.data;
            const response = axios.get("https://bluejack.binus.ac.id/lapi/api/Assistant?initial=nj23-1&generation=23-1")
            console.log(await response)
            // console.log(data);
        } catch (err: any) {
            console.log(err)
            // toast.push(err.response.data.message, {
            //     theme: {
            //         "--toastBackground": "#B02000",
            //         "--toastColor": "#fff",
            //         "--toastProgressBackground": "#fff",
            //         "--toastProgressColor": "#B02000"
            //     }
            // })
        }
    }
</script>

<div class="bg-red-sig-gradient w-screen h-screen">
    <Particle/>
    <div class="w-full h-full flex justify-center place-items-center absolute z-20">
        <div class="bg-white p-12">
            <form class="flex flex-col gap-2 w-64" on:submit|preventDefault={onSubmit}>
                <img src="{slcatering_logo}" alt="SLCatering Logo" class="h-24 object-cover"/>
                <div class="relative">
                    <div bind:this={usernameIcon}
                         class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none text-gray-400">
                        <svg fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-5 h-5">
                            <path fill-rule="evenodd"
                                  d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
                                  clip-rule="evenodd"/>
                        </svg>
                    </div>
                    <input type="text"
                           class="bg-white border border-gray-300 text-gray-900 outline-red-sig text-base rounded-sm focus:ring-red-900
                           focus:border-red-sig focused-text-red-sig block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600
                           dark:placeholder-gray-400 dark:text-white dark:focus:ring-red-900 dark:focus:border-red-sig"
                           on:focus={usernameFocus}
                           on:blur={usernameBlur}
                           bind:value="{usernameInput}"
                           placeholder="Username">
                </div>
                <div class="relative">
                    <div bind:this={passwordIcon}
                         class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none text-gray-400">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                            <path fill-rule="evenodd"
                                  d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z"
                                  clip-rule="evenodd"/>
                        </svg>

                    </div>
                    <input type="password"
                           class="bg-white border border-gray-300 text-gray-900 outline-red-sig text-base rounded-sm focus:ring-red-900
                           focus:border-red-sig focused-text-red-sig block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600
                           dark:placeholder-gray-400 dark:text-white dark:focus:ring-red-900 dark:focus:border-red-sig"
                           on:focus={passwordFocus}
                           on:blur={passwordBlur}
                           bind:value="{passwordInput}"
                           placeholder="Password">
                </div>
                <button type="submit" class="bg-red-sig p-2 text-white">
                    Login
                </button>
            </form>
        </div>
    </div>
    <footer class="w-screen h-screen flex justify-center place-items-end text-white z-10 absolute">
        <div class="mb-14 flex flex-col font-semibold place-items-center">
            <div>© Software Laboratory Catering</div>
            <div class="font-light">Developed from ❤ by NJ23-1, ML23-1.</div>
            <div class="font-light">Designed with 🦋 by NJ23-1, IC23-1.</div>
        </div>
    </footer>
</div>
