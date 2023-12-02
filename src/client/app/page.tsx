"use client";
import Image from "next/image";
import client from "@/lib/apollo";
import { LoginForm } from "./components/LoginForm";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();

  function handleLogIn() {
    //Auth logic goes here
    router.push("/dashboard");
  }

  return (
    <div className="flex flex-col items-center justify-evenly h-screen">
      <h1 className="text-3xl font-bold flex justify-center">Physifix</h1>
      <LoginForm onLogin={handleLogIn} />
    </div>
  );
}
