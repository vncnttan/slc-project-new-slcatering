import {firebaseStorage} from "$lib/firebase";
import {ref, uploadBytes, getDownloadURL} from "firebase/storage";

export async function uploadFile (
    filePath: string,
    fileName: string,
    pic: File
) {
    const fullPath = `/images/${filePath}/${fileName}.${pic.name.split(".").pop()}`
    const imageRef = ref(firebaseStorage, fullPath)
    await uploadBytes(imageRef, pic)
    return await getDownloadURL(imageRef)
}