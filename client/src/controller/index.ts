import axios from 'axios';

const BASE_URL = 'https://api.github.com/users';

export const processedModel = {
  getData: async () => {
    const API_URL = `${BASE_URL}/api/get`;

    try {
      const response = await axios.get(API_URL);
      return response;
    } catch (err) {
      console.error(err);
    }
  },
  postData: async (userValue) => {
    const API_URL = `${BASE_URL}/api/post`;

    try {
      const response = await axios.post(API_URL, { userValue });
      return response;
    } catch (err) {
      console.error(err);
    }
  },
};
