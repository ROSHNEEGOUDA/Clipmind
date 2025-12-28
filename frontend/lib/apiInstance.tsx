import axios, { AxiosInstance, AxiosRequestConfig } from "axios";

interface ApiInstance extends AxiosInstance {
  get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T>;
  post<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>;
}

const apiInstance: ApiInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000",
  timeout: 60000,
});

apiInstance.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error)
);

export default apiInstance;
