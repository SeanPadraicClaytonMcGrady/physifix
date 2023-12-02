type loginInfo = {
  username: string;
  password: string;
};

type LoginProps = {
  onLogin: (username: string, password: string) => void;
};
