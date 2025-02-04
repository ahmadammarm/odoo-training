# from odoo import http
# from odoo.http import request, Response
# import json

# class MyAPIController(http.Controller):

#     @http.route('/api/my_model', type='http', auth='public', methods=['GET'], csrf=False)
#     def get_my_model(self):
#         my_model_records = request.env['my_api_model'].search([])
#         records = []
#         for record in my_model_records:
#             records.append({
#                 'id': record.id,
#                 'name': record.name,
#                 'description': record.description,
#             })
#         return Response(json.dumps(records), content_type='application/json')

#     @http.route('/api/my_model', type='json', auth='public', methods=['POST'], csrf=False)
#     def create_my_model(self, **kwargs):
#         data = kwargs
#         new_record = request.env['my_api_model'].create({
#             'name': data.get('name'),
#             'description': data.get('description'),
#         })
#         return {'id': new_record.id, 'name': new_record.name, 'description': new_record.description}

#     @http.route('/api/my_model/<int:id>', type='http', auth='public', methods=['PUT'], csrf=False)
#     def update_my_model(self, id, **kwargs):
#         record = request.env['my_api_model'].browse(id)
#         if record:
#             record.write({
#                 'name': kwargs.get('name'),
#                 'description': kwargs.get('description'),
#             })
#             return Response(json.dumps({'status': 'success'}), content_type='application/json')
#         else:
#             return Response(json.dumps({'status': 'not found'}), content_type='application/json', status=404)

#     @http.route('/api/my_model/<int:id>', type='http', auth='public', methods=['DELETE'], csrf=False)
#     def delete_my_model(self, id):
#         record = request.env['my_api_model'].browse(id)
#         if record:
#             record.unlink()
#             return Response(json.dumps({'status': 'deleted'}), content_type='application/json')
#         else:
#             return Response(json.dumps({'status': 'not found'}), content_type='application/json', status=404)