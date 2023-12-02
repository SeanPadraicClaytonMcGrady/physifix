"use client";
import { useState } from "react";

export function LoginForm({ onLogin }: LoginProps) {
  const [loginInfo, setLoginInfo] = useState<loginInfo>({
    username: "",
    password: "",
  });

  function handleLogin(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onLogin(loginInfo.username, loginInfo.password);
  }

  return (
    <div className="">
      <form onSubmit={handleLogin} className="flex flex-col gap-2">
        <label className="flex flex-row justify-between">
          Username:
          <input
            type="text"
            name="username"
            value={loginInfo.username}
            onChange={(event) =>
              setLoginInfo({ ...loginInfo, username: event.target.value })
            }
            className="bg-gray-500 rounded-lg text-white"
          />
        </label>

        <label className="flex flex-row justify-between">
          Password:
          <input
            type="text"
            name="password"
            value={loginInfo.password}
            onChange={(event) =>
              setLoginInfo({ ...loginInfo, password: event.target.value })
            }
            className="bg-gray-500 rounded-lg text-white"
          />
        </label>
        <button type="submit" className="bg-gray-600 rounded-lg text-white">
          Submit
        </button>
      </form>
    </div>
  );
}
