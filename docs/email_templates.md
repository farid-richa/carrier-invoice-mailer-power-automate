# Email templates (step 6.8)

One email per carrier can carry several files (for example its rejected **and** its pending invoices), so the templates list the attached files instead of assuming one status. The template is picked by the contact's **Language** column.

Text in `{braces}` is dynamic content or an expression you insert in the Compose action.

## File list — Select → **File names** (inside the Yes branch, before 6.8)
- From: `body('Carrier_files')`
- Map (switch to text mode): `item()?['Name']`

In the templates, `{FILE LIST}` is:

```
join(body('File_names'), '<br>')
```

## English — Compose `Body_EN`

```html
<p>Dear {Carrier Name} team,</p>

<p>Please find attached the invoices we still have open with your company as of {RunDate}:</p>

<p>{FILE LIST}</p>

<ul>
  <li><b>Rejected invoices</b>: please send a corrected invoice or a credit note for each one, so we can process payment.</li>
  <li><b>Pending invoices</b>: please confirm they are correct or send any missing document (for example proof of delivery).</li>
</ul>

<p>Each file shows the invoice, shipment, amount and, for rejected invoices, the reason.
If anything is unclear, just reply to this email.</p>

<p>Kind regards,<br>
Freight Audit &amp; Payment team</p>
```

## Spanish — Compose `Body_ES`

```html
<p>Estimado equipo de {Carrier Name}:</p>

<p>Les adjuntamos las facturas que seguimos teniendo abiertas con su empresa a fecha {RunDate}:</p>

<p>{FILE LIST}</p>

<ul>
  <li><b>Facturas rechazadas</b>: por favor, envíennos una factura corregida o un abono por cada una para poder tramitar el pago.</li>
  <li><b>Facturas pendientes</b>: por favor, confirmen que son correctas o envíennos la documentación que falte (por ejemplo, el POD).</li>
</ul>

<p>En cada archivo aparece la factura, el envío, el importe y, en las rechazadas, el motivo.
Si tienen cualquier duda, pueden responder a este correo.</p>

<p>Un saludo,<br>
Equipo de Freight Audit &amp; Payment</p>
```

## Choosing the template — Compose `Email_body`

```
if(equals(toUpper(items('Each_carrier')?['Language']), 'ES'), outputs('Body_ES'), outputs('Body_EN'))
```
