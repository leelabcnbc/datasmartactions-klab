import jsl
from datasmart.core import schemautil

system_list = ['MI156', 'MI191']


class MouseExpRawSchemaJSL(jsl.Document):
    pass


class MouseExpRawSchemaInputJSL(jsl.Document):
    """this JSL is for input, not the final saved form."""
    schema_revision = jsl.IntField(enum=[1], required=True)  # the version of schema, in case we have drastic change
    timestamp = jsl.StringField(format="date-time", required=True)
    animal_id = jsl.StringField(required=True)
    session_id = jsl.StringField(required=True)
    acquisition_system = jsl.StringField(enum=system_list, required=True)
    acquisition_system_files = jsl.DocumentField(schemautil.filetransfer.FileListRelative, required=True)
    experiment_name = jsl.StringField(required=True)
    notebook_path = jsl.StringField(pattern=schemautil.StringPatterns.strictFilenameSensiblePattern('txt'),
                                    required=True)
    all_file_site = jsl.DocumentField(schemautil.filetransfer.FileTransferSiteRemote, required=True)
    all_file_prefix = jsl.StringField(pattern=schemautil.StringPatterns.relativePathPattern)
    session_names = jsl.DocumentField(schemautil.filetransfer.FileListRelative, required=True)
    has_real_time_data = jsl.BooleanField(required=True)
    additional_parameters = jsl.DictField(required=True)
    notes = jsl.StringField(required=True)
