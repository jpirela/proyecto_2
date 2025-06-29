import * as auth from './auth.services';
import { UserData } from './auth.interfaces';

// Register user
export const registerUser = async (req: any, res: any): Promise<void> => {
  const userData: UserData = req.body;

  try {
    const result = await auth.registerUser(userData);
    return res.status(result.code).json(result);
  } catch (error: any) {
    return res.status(400).json({ error: error.message });
  }
}

// Login user
export const setLogin = async (req: any, res: any): Promise<void> => {
  const { email, password } = req.body;

  try {
    const loginResult =  await auth.setLogin({ email, password });
    return res.status(200).json(loginResult);
  } catch (error: any) {
    const statusCode = error.code || 500;
    const errorMessage = language(error.message || "INTERNAL_SERVER_ERROR");

    return res.status(statusCode).json({ success: false, message: errorMessage });
  }
}