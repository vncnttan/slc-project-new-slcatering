<script lang="ts">
    import Particle from "../../../components/Particle.svelte";
    import slcatering_logo from "$lib/assets/slcatering_logo.png";
    import {toast} from "@zerodevx/svelte-toast";
    import axios from "axios";
    import PasswordField from "../../../components/form/PasswordField.svelte";
    import TextField from "../../../components/form/TextField.svelte";

    let passwordIcon: HTMLElement | null = null;
    let usernameInput = "";
    let passwordInput = "";


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
            const res = await axios.post("https://bluejack.binus.ac.id/lapi/api/Account/LogOn", {
                username: usernameInput,
                password: passwordInput
            }, {
                withCredentials: true
            });

            console.log(res)
        } catch {
            toast.push('Invalid email and password', {
                theme: {
                    "--toastBackground": "#B02000",
                    "--toastColor": "#fff",
                    "--toastProgressBackground": "#fff",
                    "--toastProgressColor": "#B02000"
                }
            })
        }
    }
</script>

<div class="bg-red-sig-gradient w-screen h-screen">
    <Particle/>
    <div class="w-full h-full flex justify-center place-items-center absolute z-20">
        <div class="bg-white p-12">
            <form class="flex flex-col gap-2 w-64" on:submit|preventDefault={onSubmit}>
                <img src="{slcatering_logo}" alt="SLCatering Logo" class="h-24 object-cover"/>
                <TextField bind:inputValue={usernameInput}>
                    <path fill-rule="evenodd"
                          d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
                          clip-rule="evenodd"/>
                </TextField>
                <PasswordField bind:inputValue={passwordInput}>
                    <path fill-rule="evenodd"
                          d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z"
                          clip-rule="evenodd"/>
                </PasswordField>
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
