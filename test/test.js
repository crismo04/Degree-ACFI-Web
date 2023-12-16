import vest from 'vest';

export default vest.create('paymentForm', (data = {}, changedField) => {
 vest.only(changedField);

 test('fullName', 'Full name is required', () => {
   enforce(data.fullName.value)
     .isNotBlank();
 });

 test('cardNumber', 'Card number is required', () => {
   enforce(data.cardNumber.value)
     .isNotBlank();
 });

 test('expirationDate', 'Expiration date is required', () => {
   enforce(data.expirationDate.value)
     .isNotBlank();
 });

 test('cvv', 'CVV is required', () => {
   enforce(data.cvv.value)
     .isNotBlank();
 });
});

import { submitPaymentForm } from './paymentForm';

test('submitPaymentForm', 'Form should be submitted correctly', async () => {
 const formData = {
   fullName: 'John Doe',
   cardNumber: '1234 5678 9012 3456',
   expirationDate: '12/2023',
   cvv: '123',
 };

 const result = await submitPaymentForm(formData);

 expect(result).toBe(true);
});